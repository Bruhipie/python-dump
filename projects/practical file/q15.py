emails=usernames=domains=()
n=int(input("How many emails will you input: "))
for i in range(1,n+1):
    print("Enter email for Student", i, ":", end=' ')
    email=str(input())
    emails+=(email,)
    usernames+=(email.split('@')[0],)
    domains+=(email.split('@')[1],)
print("E-mails:", emails)
print("Usernames:", usernames)
print("Domains:", domains)