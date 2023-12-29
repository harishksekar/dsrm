def stress_cpu():
    while True:
        a=1.345
        b=278.353
        c=245.231
        d=a*b*c/931.33
        result = 3.73 ** d  # Some intensive computation
        #print("CPU stress test complete.")

if __name__ == "__main__":
    stress_cpu()
