import dns.resolver
import dns.query
import dns.zone
from dns.exception import DNSException
from dns.rdataclass import *
from dns.rdatatype import *

domain = "google.com"
print "Captando NS de", domain
answers = dns.resolver.query(domain, 'NS')
ns = []
for rdata in answers:
    n = str(rdata)
    print "Encontrado el nameserver:", n
    ns.append(n)

for n in ns:
    print "\nIntentando transferir la zona del dominio %s localizada en el NS %s" % (domain, n)
    try:
        zone = dns.zone.from_xfr(dns.query.xfr(n, domain))
    except DNSException, e:
        print e.__class__, e
