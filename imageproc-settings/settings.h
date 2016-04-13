/*
 * File:   settings.h
 * Author: ronf
 *
 * Created on December 24, 2014, 3:39 PM
 */

#ifndef SETTINGS_H
#define	SETTINGS_H

#define IDENT_STR "turner-ip2.5;AMS-ENC;"

#define ROWS 1
#define COLS 8  /* for Josh Skin Proc */

#ifdef	__cplusplus
extern "C" {
#endif

#define RONF
// ronf robot radio addresses
#ifdef RONF
#define RADIO_MY_CHAN 0x13   //ron's
#define RADIO_CHANNEL 0x13 // to work with either style of channel name

#define RADIO_PAN_ID 0x2060   // ron's

//Hard code in destination address (basestation) for now, update to be dynamic later
#define RADIO_DST_ADDR 0x2011 //ron's
#define RADIO_DEST_ADDR RADIO_DST_ADDR
#define RADIO_SRC_ADDR 0x2052 //ron's
// #define RADIO_SRC_ADDR 0x3002    //cem's
#endif

#define RADIO_TXPQ_MAX_SIZE   10
#define RADIO_RXPQ_MAX_SIZE   10


//Telemetry type setup
#define TELEM_TYPE vrTelemStruct_t
#define TELEM_INCLUDE "vr_telem.h"
#define TELEMPACKFUNC(x) vrTelemGetData(x)

    // specific to robot
#define AMS_ENC_OFFSET_0 0
#define AMS_ENC_OFFSET_1 0

#ifdef	__cplusplus
}
#endif


#endif	/* SETTINGS_H */
