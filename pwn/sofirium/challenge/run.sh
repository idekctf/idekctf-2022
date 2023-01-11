#!/bin/sh

if [ -z "$1" ]
then 
    qemu-system-x86_64 \
        -m 256M\
        -kernel /home/user/bzImage \
        -initrd /home/user/initramfs.cpio  \
        -cpu kvm64,+smep,+smap \
        -append "console=ttyS0 oops=panic panic=1 kpti=1 kaslr quiet" \
        -monitor /dev/null \
        -serial mon:stdio \
        -virtfs local,path=/tmp,mount_tag=host0,security_model=passthrough,id=foobar \
        -nographic
        else 

    qemu-system-x86_64 \
        -m 256M\
        -kernel /home/user/bzImage \
        -initrd /home/user/initramfs.cpio  \
        -cpu kvm64,+smep,+smap \
        -append "console=ttyS0 oops=panic panic=1 kpti=1 kaslr quiet" \
        -drive file=$1,format=raw \
        -monitor /dev/null \
        -serial mon:stdio \
        -virtfs local,path=/tmp,mount_tag=host0,security_model=passthrough,id=foobar \
        -nographic 
fi
