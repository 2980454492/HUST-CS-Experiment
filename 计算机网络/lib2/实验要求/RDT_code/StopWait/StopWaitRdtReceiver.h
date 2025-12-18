#ifndef STOP_WAIT_RDT_RECEIVER_H
#define STOP_WAIT_RDT_RECEIVER_H
#include "RdtReceiver.h"
class StopWaitRdtReceiver :public RdtReceiver
{
private:
	// 期待收到的下一个报文序号
	int expectSequenceNumberRcvd;	
	//上次发送的确认报文
	Packet lastAckPkt;				

public:
	StopWaitRdtReceiver();
	virtual ~StopWaitRdtReceiver();

public:
	
	//接收报文，将被NetworkService调用
	void receive(const Packet &packet);	
};

#endif

