import psutil

print("<DigitalTrailBlazer>")
def view_network_cards():
    interfaces = psutil.net_if_addrs()
    for interface_name, interface_addresses in interfaces.items():
        print("网卡名称:", interface_name)
        for address in interface_addresses:
            print("    地址类型:", address.family.name)
            print("    地址:", address.address)
            print("    网络掩码:", address.netmask)
            print("    广播地址:", address.broadcast)
if __name__ == "__main__":
    view_network_cards()