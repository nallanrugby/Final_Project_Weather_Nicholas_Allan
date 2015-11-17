#Nicholas Allan 2015-11-16


all : 

%.cvs : data/%.cvs Clean_data.py 
	python Clean_data.py $< $@

%.pdf : %.csv Graph_maker.py
	python Graph_maker.py $< $@


		 		
clean:
	rm -f *.dat
	rm -f *.pdf
	