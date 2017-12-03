import dns
import dns.resolver
import dns.name
import dns.zone
import dns.query

n = dns.name.from_text('www.google.com')
o = dns.name.from_text('google.com')
print n.is_subdomain(o)
print n.is_superdomain(o)

n = dns.name.from_text('www.google.com')
o = dns.name.from_text('google.com')
rel = n.relativize(o)
n2 = rel + o
print n2 == n

print n.labels
