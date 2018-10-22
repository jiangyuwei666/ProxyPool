from schedule.proxy_schedule import Scheduler
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        print("正在安排")
        s = Scheduler()
        s.run()
    except:
        print("打开失败，再来一次")
        main()


if __name__ == '__main__':
    print("asd")
    main()
