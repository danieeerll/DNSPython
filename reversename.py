import dns
import dns.resolver
import dns.name
import dns.zone
import dns.query

import dns.reversename
n = dns.reversename.from_address("216.58.201.142")
print (n)
print (dns.reversename.to_address(n))

myResolver = dns.resolver.Resolver()
myAnswers = myResolver.query("142.201.58.216.in-addr.arpa", "PTR")
for rdata in myAnswers:
    print rdata
