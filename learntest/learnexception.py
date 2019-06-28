def main(x):
    status = "success"
    try:
        result = 1 / x
        print("main")
        return result
    except Exception:
        status = "fail"
        raise
    finally:
        print(status)


if __name__ == '__main__':
    main(1)
    main(0)