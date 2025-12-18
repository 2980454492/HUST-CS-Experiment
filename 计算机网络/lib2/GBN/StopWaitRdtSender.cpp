#include "stdafx.h"
#include "Global.h"
#include "StopWaitRdtSender.h"

// 构造函数：初始化GBN发送方
GBNRdtSender::GBNRdtSender() : base(0), expectSequenceNumberSend(0), waitingState(false)
{
	// 初始化等待确认的数据包数组，将序列号设为-1表示空位
	for (int i = 0; i < 2 * Configuration::WINDOW_LEN; i++)
	{
		packetWaitingAck[i].seqnum = -1;
	}
}

GBNRdtSender::~GBNRdtSender()
{
}

// 获取等待状态：判断发送窗口是否已满
bool GBNRdtSender::getWaitingState()
{
	return waitingState;
}

// 发送消息：将应用层消息封装成数据包并发送
bool GBNRdtSender::send(const Message& message)
{
	if (this->waitingState) // 窗口已满，无法发送任何数据
	{
		return false;
	}

	const int& window_len = Configuration::WINDOW_LEN; // 窗口大小简写
	const int seq_len = 2 * Configuration::WINDOW_LEN; // 序列号空间大小（2倍窗口长度）
	const int send_num = expectSequenceNumberSend % seq_len; // 当前要发送的报文在窗口中的位置

	// 如果当前要发送的序号在窗口范围内，准备数据包[1,4](@ref)
	if (expectSequenceNumberSend < window_len + base)
	{
		// 设置数据包各字段
		this->packetWaitingAck[send_num].acknum = -1; // 确认号字段在发送方数据包中忽略
		this->packetWaitingAck[send_num].seqnum = this->expectSequenceNumberSend; // 设置序列号
		this->packetWaitingAck[send_num].checksum = 0; // 先设0，计算校验和后再更新
		memcpy(this->packetWaitingAck[send_num].payload, message.data, sizeof(message.data)); // 拷贝数据载荷
		this->packetWaitingAck[send_num].checksum = pUtils->calculateCheckSum(this->packetWaitingAck[send_num]); // 计算校验和
		pUtils->printPacket("发送方发送报文", this->packetWaitingAck[send_num]);
	}

	// 如果当前没有等待确认的数据包（base等于期望发送序号），启动定时器[4](@ref)
	if (base == expectSequenceNumberSend)
	{
		pns->startTimer(SENDER, Configuration::TIME_OUT, this->packetWaitingAck[send_num].seqnum);
	}

	// 发送数据包到网络层
	pns->sendToNetworkLayer(RECEIVER, this->packetWaitingAck[send_num]);

	expectSequenceNumberSend++; // 更新下一个要发送的序号

	// 检查窗口是否已满（已发送但未确认的数据包达到窗口大小）
	if (expectSequenceNumberSend == window_len + base)
	{
		this->waitingState = true; // 进入等待状态，暂停接收应用层数据
	}
	return true;
}

// 接收确认包：处理来自接收方的确认[1,4](@ref)
void GBNRdtSender::receive(const Packet& ackPkt)
{
	const int& window_len = Configuration::WINDOW_LEN;
	const int seq_len = 2 * Configuration::WINDOW_LEN;

	// 检查校验和是否正确
	int checkSum = pUtils->calculateCheckSum(ackPkt);

	// 如果校验和正确，并且确认序号 >= 当前基序号（避免处理过时的确认）
	if (checkSum == ackPkt.checksum && ackPkt.acknum >= this->base)
	{
		this->waitingState = false; // 退出等待状态，可以继续接收应用层数据
		pUtils->printPacket("发送方正确收到确认", ackPkt);

		pns->stopTimer(SENDER, this->base); // 停止当前基序号的定时器

		// 如果还有未确认的数据包，为下一个未确认的包启动定时器[4](@ref)
		if (expectSequenceNumberSend > 1 + ackPkt.acknum)
		{
			pns->startTimer(SENDER, Configuration::TIME_OUT, 1 + ackPkt.acknum);
		}

		this->base = 1 + ackPkt.acknum; // 滑动窗口基序号（累积确认机制）

		// 清理滑动窗口之外的数据包缓存（将序列号设为-1）
		for (int i = window_len + this->base; i < seq_len + this->base; i++)
		{
			this->packetWaitingAck[i % seq_len].seqnum = -1;
		}

		// 打印当前滑动窗口状态（用于调试和观察）
		cout << "滑动窗口移至: { ";
		for (int i = base; i < window_len + base; i++)
		{
			if (this->packetWaitingAck[i % seq_len].seqnum != -1)
			{
				cout << this->packetWaitingAck[i % seq_len].seqnum << ' ';
			}
			else
			{
				cout << '_' << ' '; // 空位用下划线表示
			}
		}
		cout << "}" << endl;
	}
}

// 超时处理函数：当定时器超时时调用[4](@ref)
void GBNRdtSender::timeoutHandler(int seqNum)
{
	// GBN协议特点：只有一个定时器，用于监控最早未确认的包
	// 当超时时，重传所有已发送但未确认的数据包（从base到expectSequenceNumberSend-1）
	const int& window_len = Configuration::WINDOW_LEN;
	const int seq_len = 2 * Configuration::WINDOW_LEN;

	pns->stopTimer(SENDER, seqNum); // 停止当前定时器
	pns->startTimer(SENDER, Configuration::TIME_OUT, seqNum); // 重新启动定时器

	// 重传窗口中所有未确认的数据包（回退N步）[1,4](@ref)
	for (int i = this->base; i < this->expectSequenceNumberSend; i++)
	{
		pUtils->printPacket("发送方定时器时间到，重发报文", this->packetWaitingAck[i % seq_len]);
		pns->sendToNetworkLayer(RECEIVER, this->packetWaitingAck[i % seq_len]);
	}
}