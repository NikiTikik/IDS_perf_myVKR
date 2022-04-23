import Pyro4

from service_funcs import Service_funcs
# suricata_status()
# suricata_start()
# suricata_stop()
# ids_status()
# ids_start()
# ids_stop()
# calc_integr()

from rules_funcs import Rules_funcs
# disable_all_rules()
# enable_all_rules()
# disable_class(class)
# enable_class(class)
# disable_sid(sid)
# enable_sid(sid)
# ids_rulesreload()

from bd_funcs import BD_funcs
# count_total_events(start_time=start_time, end_time=end_time)
# count_uniq_events(start_time=start_time, end_time=end_time)
# last_cid()


class Simple_functions(object):
    def Simple(self, var1):
        return(int(var1)*8)


def main():

    Class_Simple_functions = Pyro4.expose(Simple_functions)
    Class_Service_funcs = Pyro4.expose(Service_funcs)
    Class_Rules_funcs = Pyro4.expose(Rules_funcs)
    Class_BD_funcs = Pyro4.expose(BD_funcs)

    Pyro4.Daemon.serveSimple(
        {
            Class_Simple_functions: 'Simple_functions',
            Class_Service_funcs: 'Service_funcs',
            Class_Rules_funcs: 'Rules_funcs',
            Class_BD_funcs: 'BD_Funcs',
        },
        host='10.0.223.111',
        port=9999,
        ns=False
        )

    # start server
    Pyro4.Daemon.requestLoop()


main()
