clean:
	@rm -f *.orig *~
	@find . -type f -name '*.orig' -o -name '*~' -exec rm -fv {} \;
