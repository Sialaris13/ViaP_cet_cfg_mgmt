from jinja import load_data, render, write_config

# get data from files
data = load_data("essex_nj")


config = render("router/router_config.j2", data)
write_config(config, "router_config.cfg")


config = render("firewall/WAN_IN_FW_config.j2", data)
write_config(config, "WAN_FW_POLICY_config.cfg")


config = render("router/dns.j2", data)
write_config(config, "router_dns.cfg")
