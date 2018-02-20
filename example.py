from parser import Parser

root = Parser.parse("(asciitree (  sometimes you) (just (want to draw)) trees (in (your terminal)))")
root.print()
