#ifndef STOP_WAIT_RDT_SENDER_H
#define STOP_WAIT_RDT_SENDER_H
#include "RdtSender.h"
class StopWaitRdtSender :public RdtSender
{
private:
	// 下一个发送序号 
	int expectSequenceNumberSend;	
	// 是否处于等待Ack的状态
	bool waitingState;				
	//已发送并等待Ack的数据包
	Packet packetWaitingAck;		

public:

	bool getWaitingState();
	//发送应用层下来的Message，由NetworkServiceSimulator调用,如果发送方成功地将Message发送到网络层，返回true;如果因为发送方处于等待正确确认状态而拒绝发送Message，则返回false
	bool send(const Message &message);	
	//接受确认Ack，将被NetworkServiceSimulator调用	
	void receive(const Packet &ackPkt);					
	//Timeout handler，将被NetworkServiceSimulator调用
	void timeoutHandler(int seqNum);					

public:
	StopWaitRdtSender();
	virtual ~StopWaitRdtSender();
};

#endif

