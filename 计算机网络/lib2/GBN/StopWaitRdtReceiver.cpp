#include "stdafx.h"
#include "Global.h"
#include "StopWaitRdtReceiver.h"

// GBN接收方构造函数
GBNRdtReceiver::GBNRdtReceiver() : expectSequenceNumberRcvd(0)  // 初始化期望接收的序列号为0
{
    // 初始化上一次发送的确认包
    lastAckPkt.acknum = -1;  // 初始确认号为-1，表示尚未接收任何有效数据包
    lastAckPkt.checksum = 0; // 校验和初始为0
    lastAckPkt.seqnum = -1;  // 序列号字段在确认包中通常被忽略

    // 初始化确认包的载荷内容
    for (int i = 0; i < Configuration::PAYLOAD_SIZE; i++)
    {
        lastAckPkt.payload[i] = '.';  // 用特定字符填充载荷
    }
    // 计算确认包的完整校验和
    lastAckPkt.checksum = pUtils->calculateCheckSum(lastAckPkt);
}

// GBN接收方析构函数
GBNRdtReceiver::~GBNRdtReceiver()
{
}

// 接收数据包的主要处理函数
void GBNRdtReceiver::receive(const Packet& packet)
{
    // 计算接收到的数据包的校验和，用于错误检测[2,4](@ref)
    int checkSum = pUtils->calculateCheckSum(packet);

    // 情况1：校验和正确且序列号符合期望（按序到达的正确数据包）
    if (checkSum == packet.checksum && this->expectSequenceNumberRcvd == packet.seqnum)
    {
        // 打印正确接收的报文信息
        pUtils->printPacket("接收方正确收到发送方的报文", packet);

        // 从数据包中提取消息载荷，准备递交应用层[3](@ref)
        Message msg;
        memcpy(msg.data, packet.payload, sizeof(packet.payload));

        // 将消息递交给应用层[2](@ref)
        pns->delivertoAppLayer(RECEIVER, msg);

        // 更新确认包：确认号设置为刚接收的数据包序列号[4](@ref)
        lastAckPkt.acknum = packet.seqnum;

        // 重新计算确认包的校验和
        lastAckPkt.checksum = pUtils->calculateCheckSum(lastAckPkt);

        // 打印即将发送的确认报文信息
        pUtils->printPacket("接收方发送确认报文", lastAckPkt);

        // 通过网络层向发送方发送确认包[3](@ref)
        pns->sendToNetworkLayer(SENDER, lastAckPkt);

        // 更新期望接收的下一个序列号[4](@ref)
        this->expectSequenceNumberRcvd++;
    }
    else  // 情况2：数据包出错或序列号不符合期望
    {
        // 根据错误类型打印相应信息
        if (checkSum != packet.checksum)
        {
            pUtils->printPacket("接收方没有正确收到发送方的报文,数据校验错误", packet);
        }
        else
        {
            pUtils->printPacket("接收方没有正确收到发送方的报文,报文序号不对", packet);
        }

        // 打印重新发送上次确认包的信息[4](@ref)
        pUtils->printPacket("接收方重新发送上次的确认报文", lastAckPkt);

        // 重新发送上一次的确认包（GBN协议特点：对错误或乱序包发送最近的正确ACK）[4,5](@ref)
        pns->sendToNetworkLayer(SENDER, lastAckPkt);
    }
}