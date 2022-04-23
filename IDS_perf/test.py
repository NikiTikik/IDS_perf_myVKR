#!/usr/bin/env python

from helper_funcs import connect_SSH, get_SSH_response, close_SSH, restart_SSH, get_SSH_send
from perf_funcs import run_tcpreplay, run_ping, run_parallel, connect_via_Pyro
from excell import excell_table

bd_funcs = connect_via_Pyro("BD_Funcs")
serv_funcs = connect_via_Pyro("Service_funcs")

print('\nsuricata is running: ' + str(serv_funcs.suricata_status()) + '\n')
# print(t3.ids_rulesreload())


def test1_in(speed, loop, filename, number):

    s_cid = bd_funcs.last_cid()
    print('start_cid: ' + str(int(s_cid)))

    tcprelay_params = {"speed": speed,
                       "loop": loop,
                       "filename": filename
                       }
    ping_params = {"number": number}

    run_parallel(run_tcpreplay, tcprelay_params, run_ping, ping_params)

    # parall_proc_universal(TcpreplyThread, tcprelay_params, PingThread, ping_params)
    
    while bd_funcs.barnyard2_finish() == False:
        print('\nbarnyard2 has finished: ' + str(bd_funcs.barnyard2_finish()) + '\n')
    print('\nbarnyard2 has finished: ' + str(bd_funcs.barnyard2_finish()) + '\n')

    f_cid = bd_funcs.last_cid()

    # 3) it takes the number of last cid from database "barnyard2" on IDS again
    print('finish_cid: ' + str(int(f_cid)) + '\n')
    all_cid = f_cid - s_cid
    # 4) it calculates difference of results (point 1 and 2)
    print('events: ' + str(int(all_cid)) + ' on speed ' + str(int(speed)) + ' Mbit/s\n')
    print('****************************')

    return all_cid


def test1(loop, filename, number, min_speed=25, max_speed=800, step=25):

    result = []
    all_speed = []

    for i in range(min_speed, max_speed, step):
        # Here elementary test play several times. It sets speed of traffic,
        result.append(test1_in(i, loop, filename, number))

        # filename of dump-file and number of ping packets.
        all_speed.append(i)
    excell_table(result, all_speed)

test1(2, "bigFlows.pcap", 1000, 400, 451, 50)