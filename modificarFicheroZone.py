import dns.zone
from dns.exception import DNSException
from dns.rdataclass import *
from dns.rdatatype import *

domain = "example.com"
print "Cogiendo la zona del dominio ", domain
zone_file = "%s" % domain

try:
    zone = dns.zone.from_file(zone_file, domain)
    print "Origen de la zona:", zone.origin

    for (name, ttl, rdata) in zone.iterate_rdatas(SOA):
        serial = rdata.serial
        new_serial = serial + 1
        print "Cambiando serial del SOA de %d a %d" % (serial, new_serial)
        rdata.serial = new_serial

    node_delete = "www2"
    print "Eliminando nodo", node_delete
    zone.delete_node(node_delete)

    A_change = "mail"
    new_IP = "192.168.2.100"
    print "Cambiando IPV4 del nodo", A_change, "al", new_IP
    rdataset = zone.find_rdataset(A_change, rdtype=A)
    for rdata in rdataset:
        rdata.address = new_IP

    rdataset = zone.find_rdataset("@", rdtype=NS)
    new_ttl = rdataset.ttl / 2
    print "Cambiando el TTL de todos los NS a", new_ttl
    rdataset.ttl = new_ttl

    A_add = "www3"
    print "Añadir nuevo nodo www3:", A_add
    rdataset = zone.find_rdataset(A_add, rdtype=A, create=True)
    rdata = dns.rdtypes.IN.A.A(IN, A, address="192.168.10.30")
    rdataset.add(rdata, ttl=86400)

    new_zone_file = "new.%s" % domain
    zone.to_file(new_zone_file)
except DNSException, e:
        print e.__class__, e
