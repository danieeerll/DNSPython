import dns.zone
from dns.exception import DNSException
from dns.rdataclass import *
from dns.rdatatype import *

domain = "example.com"
print "Consiguiendo la zona del dominio ", domain
zone_file = "%s" % domain

try:
    zone = dns.zone.from_file(zone_file, domain)
    print "Origen de zona:", zone.origin
    for name, node in zone.nodes.items():
        rdatasets = node.rdatasets
        print "\n**** NUEVO NODO ****"
        print "Nombre del nodo:", name
        for rdataset in rdatasets:
            print "--- NUEVO RDATASET ---"
            print "rdataset string:", rdataset
            print "rdataset rdclass:", rdataset.rdclass
            print "rdataset rdtype:", rdataset.rdtype
            print "rdataset ttl:", rdataset.ttl
            print "rdataset tiene la siguiente rdata:"
            for rdata in rdataset:
                print "-- EMPEZANDO RDATA --"
                print "rdata string:", rdata
                if rdataset.rdtype == SOA:
                    print "** SOA rdata **"
                    print "expire:", rdata.expire
                    print "minimum:", rdata.minimum
                    print "mname:", rdata.mname
                    print "refresh:", rdata.refresh
                    print "retry:", rdata.retry
                    print "rname:", rdata.rname
                    print "serial:", rdata.serial
                if rdataset.rdtype == MX:
                    print "** MX rdata **"
                    print "exchange:", rdata.exchange
                    print "preference:", rdata.preference
                if rdataset.rdtype == NS:
                    print "** NS rdata **"
                    print "target:", rdata.target
                if rdataset.rdtype == CNAME:
                    print "** CNAME rdata **"
                    print "target:", rdata.target
                if rdataset.rdtype == A:
                    print "** A rdata **"
                    print "address:", rdata.address
except DNSException, e:
    print e.__class__, e
