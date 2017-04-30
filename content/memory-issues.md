Title: Adding randomizers to cmdchallenge
Status: draft
Date: 2017-05-10
Slug: never-open-up-ssh


```bash
root       460  0.1 18.2 266968 186424 ?       Ss   Apr01  13:44 /usr/lib/systemd/systemd-journald
```

```bash
pmap -d $(pidof systemd-journald)
```

```bash
Apr 07 21:29:00 ip-172-31-24-119.ec2.internal sshd[5977]: PAM 2 more authentication failures; logname
Apr 07 21:29:00 ip-172-31-24-119.ec2.internal sshd[5979]: Failed password for root from 58.218.199.13
Apr 07 21:29:01 ip-172-31-24-119.ec2.internal sshd[5979]: Received disconnect from 58.218.199.133 por
Apr 07 21:29:01 ip-172-31-24-119.ec2.internal sshd[5979]: Disconnected from 58.218.199.133 port 37209
Apr 07 21:29:01 ip-172-31-24-119.ec2.internal sshd[5979]: PAM 2 more authentication failures; logname
Apr 07 21:29:04 ip-172-31-24-119.ec2.internal sshd[5983]: pam_tally2(sshd:auth): Tally overflowed for
Apr 07 21:29:04 ip-172-31-24-119.ec2.internal sshd[5983]: pam_unix(sshd:auth): authentication failure
Apr 07 21:29:06 ip-172-31-24-119.ec2.internal systemd[1]: Started OpenSSH per-connection server daemo
Apr 07 21:29:06 ip-172-31-24-119.ec2.internal sshd[5983]: Failed password for root from 58.218.199.13
Apr 07 21:29:06 ip-172-31-24-119.ec2.internal sshd[5983]: pam_tally2(sshd:auth): Tally overflowed for
Apr 07 21:29:08 ip-172-31-24-119.ec2.internal sshd[5983]: Failed password for root from 58.218.199.13
````

