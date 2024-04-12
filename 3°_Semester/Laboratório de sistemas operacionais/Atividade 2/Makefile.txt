# Compilador C
clang = clang

# Opções de compilação
CFLAGS = -Wall -std=c11

# Compilar o programa "helloWorld.c"
helloWorld:
	$(clang) $(CFLAGS) -o hello helloWorld.c

# Compilar o programa "main.c"
main:
	$(clang) $(CFLAGS) -o main main.c

# Executar o programa "main"
run:
	./main

# Limpeza do executáveis
clean:
	rm -f hello main


