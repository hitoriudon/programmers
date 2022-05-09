
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

time_t cur_time; // 전역변수

void print_int() {
    int i = 0, max = 2;
    for (i = 0; i < max; i++) {
        sleep(2);
        printf ( "[value = %d] [time = %2d]\n", i, time(NULL) - cur_time );
    }
}

void print_char() {
    int i = 0, max = 2;
    for (i = 0; i < max; i++) {
        sleep(3);
        printf ( "[value = %c] [time = %2d]\n", i+'A', time(NULL) - cur_time );
    }
}

int main (int argc, char** argv) {
    
    pthread_t int_thread, char_thread;
    int ret;

    cur_time = time (NULL);
    ret = pthread_create ( &char_thread, NULL, (void*)print_char, NULL);
    sleep(1);
    ret=pthread_create ( &int_thread, NULL, (void*)print_int, NULL);
    
    pthread_join(int_thread, NULL);
    pthread_join(char_thread, NULL);
}