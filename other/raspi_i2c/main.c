#include <stdio.h>
#include <wiringPiI2C.h>

// プロトタイプ宣言
unsigned int getSlaveUINT(int);

#define	SLAVE_NUM	2

int main (void) {
	// I2C接続
	int fd[SLAVE_NUM];
	fd[0] = wiringPiI2CSetup(0x30);
	fd[1] = wiringPiI2CSetup(0x31);

	// 接続の確認
	for (int i = 0; i < SLAVE_NUM; i++) {
		printf("No.%d\n", fd[i]);
		if (fd[i] == -1) {
			printf("I2C接続に失敗しました。\n");
			return 1;
		}
	}

	unsigned int data[SLAVE_NUM];

	for (int i = 0; i < SLAVE_NUM; i++) {
		data[i] = getSlaveUINT(fd[i]);
	}
	printf("%d\n", data[0]);

	return 0;
}


// I2Cでスレーブからの複数バイトデータ受信
unsigned int getSlaveUINT (int fd) {
	unsigned int data = 0;
        for (int i = 0; i < 2; i++) {
                data += (wiringPiI2CRead(fd) << (8 * i));
        }
	return data;
}
