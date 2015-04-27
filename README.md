dict-redis-lfu is a tool for console dictionary. At the same time, it implements word list you searched using Redis.

Dictonary
----------
The backend is "www.bing.com/dict",  and I retrive all needed infomation from this page.

Word List
------------
When you search one word, it will add the word in a sorted set in Redis. So if you want it work, start the redis-server first.

It use Least-Frequently Used (LFU) cache algorithm to discard word.

> Counts how often an item is needed. Those that are used least often
> are discarded first.
> ----http://en.wikipedia.org/wiki/Cache_algorithms

NOTE: If you don't start `redis-server`,  lookup word will OK, but history will lost.

Usage
-------
1. help page
	```
	$ dict -h
	Usage: dict [options] [word]
	
	lookup dictionary
	
	Options:
	  -h, --help  show this help message and exit
	  -l, --list  dump word list
	```
	 

2. lookup word
	```
	 $ dict test
	US [test] UK [test]
	试验；测试；检测；测验
	试验；检测；考试；测验
	检验；考验；睾酮(testosterone)
	
	Variety:
		Plural Form：tests  Past Tense：tested  Present Participle：testing
	Synonyms:
		pass test,take test,test method,do test,fail test,preliminary test,standard test,real test,acid test,final test,thoroughly test,carefully test,examination,exam,tryout,trial run,proof,try,try out,put to the test,examine,assess
	E-C:
		1.考试; 测验
		2.【医】(医学的)检查; 医学鉴定; 化验
		3.试验; 检测
		4.艰难处境; 考验; 试金石
		5.【板】板球赛,常用于英式英语
		6.【动】(软体动物的)壳
	E-E:
		1.a series of questions, problems, or practical tasks to gauge sb.'s knowledge, ability, or experience
		2.[Medical &amp; Healthcare]an examination of part of the body or of a body fluid or specimen in order to find sth. out
		3.a trial run-through of a process or on equipment to find out if it works
		4.a difficult situation that shows what qualities sb. or sth. has
		5.[Cricket]refers to a test match, usually used in British English
		6.[Animal]the hard outer covering or shell of some invertebrates, e.g. mollusks and crustaceans
	```

3. get word list(default top 50)
	```
	$ dict -l                                                                                                                                                 
	0. fangfang	 10
	1. haha	 3
	2. tacked	 1
	3. coat	 1
	4. xetex	 1
	5. wahaha	 1
	6. stainless	 1
	7. ride	 1
	```
License: BSD
Author: vonnyfly <lifeng1519@gmail.com>
