obj-m:= myled.o                           #オブジェクトファイルの名前を指定（拡張子はo）

myled.ko: myled.c
	make -C /usr/src/linux-headers-4.4.0-1046-raspi2 M=`pwd` V=1 modules     #makeと打つと実行される
clean:
	make -C /usr/src/linux-headers-4.4.0-1046-raspi2 M=`pwd` V=1 clean        #make cleanで
