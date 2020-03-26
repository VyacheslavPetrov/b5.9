import time

def time_this(kek):
	def decorator(fn):
		avg_time = 0
		for i in range(fn):
			t0 = time.time()
			kek(fn)
			t1 = time.time()
			avg_time += (t1 - t0)
		avg_time /= (fn)
		print("Выполнение заняло %.5f секунд" %avg_time)
	return decorator

@time_this
def f(fn):
    for j in range(1000000):
        pass

f(10)