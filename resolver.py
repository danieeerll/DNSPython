import dns
import dns.resolver
import dns.name
import dns.zone
import dns.query

print "-----------------------------------------"
print "MX - registro de intercambio de correo"
res = dns.resolver.query('google.com','MX')
for rdata in res:
    print ('Host: ', rdata.exchange, 'has preference', rdata.preference)
    

print "-----------------------------------------"
print "NS - registros de name server"
resns = dns.resolver.query('google.com','NS')
for rdata in resns:
    print (rdata)

print "-----------------------------------------"
print "A - direccin ip"
resa = dns.resolver.query('google.com','A')
for rdata in resa:
    print (rdata)

print "-----------------------------------------"
print "AAAA - direccin ipv6"
resaaaa = dns.resolver.query('google.com','AAAA')
for rdata in resaaaa:
    print (rdata)

print "-----------------------------------------"
print "SOA - registro SOA (Informacion sobre el DNS)"
ressoa = dns.resolver.query('google.com','SOA')
for rdata in ressoa:
    print ' serial: %s  tech: %s' % (rdata.serial, rdata.rname)
    print ' refresh: %s  retry: %s' % (rdata.refresh, rdata.retry)
    print ' expire: %s  minimum: %s' % (rdata.expire, rdata.minimum)
    print ' mname: %s' % (rdata.mname)

print "-----------------------------------------"
print("TXT - registro TXT del dominio")
restxt = dns.resolver.query('google.com','TXT')
for rdata in restxt:
    print 'TXT: ', rdata

print "-----------------------------------------"
print("CNAME - registro CNAME del dominio")
rescname = dns.resolver.query('mail.google.com','CNAME')
for rdata in rescname:
    print ' cname target address:', rdata.target

