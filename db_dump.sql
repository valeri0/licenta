-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: my_app
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('6629488c7415');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chapter`
--

DROP TABLE IF EXISTS `chapter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chapter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chapter`
--

LOCK TABLES `chapter` WRITE;
/*!40000 ALTER TABLE `chapter` DISABLE KEYS */;
INSERT INTO `chapter` VALUES (1,'Intro'),(2,'Operators and Expressions'),(3,'Logic'),(4,'Control flow'),(5,'Functions'),(6,'Srings');
/*!40000 ALTER TABLE `chapter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chapter_exercise`
--

DROP TABLE IF EXISTS `chapter_exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chapter_exercise` (
  `exercise_id` int(11) NOT NULL,
  `chapter_id` int(11) NOT NULL,
  PRIMARY KEY (`exercise_id`,`chapter_id`),
  KEY `chapter_id` (`chapter_id`),
  CONSTRAINT `chapter_exercise_ibfk_1` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`),
  CONSTRAINT `chapter_exercise_ibfk_2` FOREIGN KEY (`chapter_id`) REFERENCES `chapter` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chapter_exercise`
--

LOCK TABLES `chapter_exercise` WRITE;
/*!40000 ALTER TABLE `chapter_exercise` DISABLE KEYS */;
INSERT INTO `chapter_exercise` VALUES (5,1),(6,1),(2,2),(4,2),(1,3),(3,3),(12,4),(10,5),(7,6),(8,6),(9,6),(11,6);
/*!40000 ALTER TABLE `chapter_exercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chapter_lesson`
--

DROP TABLE IF EXISTS `chapter_lesson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chapter_lesson` (
  `chapter_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  PRIMARY KEY (`chapter_id`,`lesson_id`),
  KEY `chapter_lesson_fk2_idx` (`lesson_id`),
  CONSTRAINT `chapter_lesson_fk1` FOREIGN KEY (`chapter_id`) REFERENCES `chapter` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `chapter_lesson_fk2` FOREIGN KEY (`lesson_id`) REFERENCES `lesson` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chapter_lesson`
--

LOCK TABLES `chapter_lesson` WRITE;
/*!40000 ALTER TABLE `chapter_lesson` DISABLE KEYS */;
INSERT INTO `chapter_lesson` VALUES (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(2,11),(2,12),(2,13),(2,14),(2,15),(2,16),(2,17),(4,18),(4,19),(4,20),(4,21),(4,22),(4,23),(4,24),(4,25);
/*!40000 ALTER TABLE `chapter_lesson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercise`
--

DROP TABLE IF EXISTS `exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exercise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `content` mediumtext,
  `source_code` mediumtext,
  `default_elo_rating` float DEFAULT NULL,
  `solved_source_code` mediumtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercise`
--

LOCK TABLES `exercise` WRITE;
/*!40000 ALTER TABLE `exercise` DISABLE KEYS */;
INSERT INTO `exercise` VALUES (1,'Sleep in','The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we\'re on vacation. Return True if we sleep in.','def sleep_in(weekday, vacation):   ',600,'\ntest_case = [(True, True), (False, False), (False, True), (True, False)]\n\ndef sleep_in(weekday, vacation):   \n	if not weekday or vacation:   \n		return True   \n	else:     \n		return False'),(2,'Sum double','Given two int values, return their sum. Unless the two values are the same, then return double their sum.','def sum_double(a,b):',600,'\ntest_case = [(1,2),(1,3),(1000,-100),(20,20),(0,0),(100,100)]\n\ndef sum_double(a, b):\n  # Store the sum in a local variable\n  sum = a + b\n  \n  # Double it if a and b are the same\n  if a == b:\n    sum = sum * 2\n  return sum'),(3,'Monkey Trouble','We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.','def monkey_trouble(a_smile, b_smile):   ',600,'\ntest_case = [(False,False),(True,True),(True,False),(False,True)]\n\ndef monkey_trouble(a_smile, b_smile):\n  if a_smile and b_smile:\n    return True\n  if not a_smile and not b_smile:\n    return True\n  return False\n  '),(4,'Makes10','Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.','def makes10(a, b):\n  \n',600,'\ntest_case = [(10,2),(9,9),(4,5),(5,6),(4,6),(-2,12)]\n\ndef makes10(a, b):\n  return (a == 10 or b == 10 or a+b == 10)\n  '),(5,'Parrot Trouble','We have a loud talking parrot. \nThe \"hour\" parameter is the current hour time in the range 0..23. \nWe are in trouble if the parrot is talking and the hour is before 7 or after 20. \nReturn True if we are in trouble.','def parrot_trouble(talking, hour):\n  \n',600,'\ntest_case = [(True,10),(True,2),(False,2),(True,20),(False,21),(True,0)]\n\ndef parrot_trouble(talking, hour):\n  return (talking and (hour < 7 or hour > 20))\n  \n'),(6,'Near Hundred','Given an int n, return True if it is within 10 of 100 or 200. \nNote: abs(num) computes the absolute value of a number.','def near_hundred(n):\n\n',1500,'\n\ntest_case = [(90,),(80,),(20,),(30,),(510,),(99,)]\n\ndef near_hundred(n):\n  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))\n \n'),(7,'Not String','Given a string, return a new string where \"not \" has been added to the front. \nHowever, if the string already begins with \"not\", return the string unchanged. .','def not_string(str):\n\n',1500,'\ntest_case = [(\"not\",),(\"notanot\",),(\"parrot\",),(\"hello\",),(\"notfunnyman\",)]\n\ndef not_string(str):\n  if len(str) >= 3 and str[:3] == \"not\":\n    return str\n  return \"not \" + str\n'),(8,'String Times','Given a string and a non-negative int n, return a larger string that is n copies of the original string.','def string_times(str, n):\n  \n',1700,'\ntest_case = [(\"not\",2),(\"notanot\",4),(\"parrot\",1),(\"hello\",5),(\"notfunnyman\",6)]\n\ndef string_times(str, n):\n  result = \"\"\n  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]\n    result = result + str  # could use += here\n  return result\n'),(9,'Hello Name','Given a string name, e.g. \"Bob\", return a greeting of the form \"Hello Bob!\". ','def hello_name(name):\n  \n  \n',600,'\ntest_case = [(\"not\",),(\"notanot\",),(\"parrot\",),(\"hello\",),(\"notfunnyman\",)]\n\ndef hello_name(name):\n	return \"Hello \" + name;\n'),(10,'Make tags','The web is built with HTML strings like \"<i>Yay</i>\" which draws Yay as italic text. \nIn this example, the \"i\" tag makes <i> and </i> which surround the word \"Yay\". \nGiven tag and word strings, create the HTML string with tags around the word, e.g. \"<i>Yay</i>\". ','def make_tags(tag, word):\n  \n  \n',1100,'\ntest_case = [(\"i\",\"Huha\"),(\"quote\",\"To be or not to be),(\"p\",\"pp\"),(\"h19\",\"wOw\"),(\"i\",\"uh\")]\n\ndef make_tags(tag, word):\n	return \"<{0}>{1}</{0}>\".format(tag,word)\n'),(11,'First Two','Given a string, return the string made of its first two chars, so the String \"Hello\" yields \"He\". \nIf the string is shorter than length 2, return whatever there is, \nso \"X\" yields \"X\", and the empty string \"\" yields the empty string \"\". ','def first_two(str):\n  \n  \n',1000,'\ntest_case = [(\"123\",),(\"as\",),(\"adsasda\",),(\"1234\",),(\"0\",),(\"oo\",)]\n\ndef first_two(str):\n	if len(str) >= 2:\n		return str[:2]\n	else:\n		return str\n'),(12,'Cigar Party','When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. \nReturn True if the party with the given values is successful, or False otherwise.','def cigar_party(cigars, is_weekend):\n	\n  \n',800,'\ntest_case = [(30,False),(40,True),(90,False),(90,True),(45,True),(1,False)]\n\ndef cigar_party(cigars, is_weekend):\n	if weekend:\n		if cigars >= 40:\n			return True\n	elif cigars >= 40 and cigars <= 60:\n		return True\n\n	return False\n');
/*!40000 ALTER TABLE `exercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lesson`
--

DROP TABLE IF EXISTS `lesson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `content` mediumtext,
  `instructions` mediumtext,
  `source_code` mediumtext,
  `DEFAULT_ELO_RATING` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lesson`
--

LOCK TABLES `lesson` WRITE;
/*!40000 ALTER TABLE `lesson` DISABLE KEYS */;
INSERT INTO `lesson` VALUES (1,'Introduction','If all you know about a computer is how to turn it on and shut it down, no problem, here you will learn how to write code in the Python programming language, solving real world problems and getting the taste of coding really fast.\n\nWhat is Python?\n\n\nPython is probably one of the few programming languages which is both simple and powerful. This is good for beginners as well as for experts, and more importantly, is fun to program with. The next lessons will aim to help you learn this wonderful language and show how to get things done quickly and painlessly.','As you can see in the right there is a editor where you will write the Python code.\n\nPressing the \"Test\" button will immediately return your result in the console below the \"Submit\" button will send the code to our servers to evaluate your code and track your progress','# Do not be worry about all these symbols written here\n# We will get to the bottom of these asap\n# Just hit \"Submit\" for now!\n\nprint(\"Hello Friend!\")',100),(2,'Print statements','<p>A Python program is composed of statements.</p>\n<br>\n<p>Think of a statement as an instruction</p>\n<br>\n<p>\nIn our first program, we have only one statement: the <span class=\"source_code\">print</span> statement.\n</p>\n<br>\n\n<p>\n<span class=\"source_code\">print</span> is the function that displays something from your code\nto the computer, basically as you are saying to your computer \"Tell me this\", \"Tell me that\"<br>\nReplace \"Tell me\" with <span class=\"source_code\">print</span> and \"this\" with anything and you will<br>\nget <span class=\"source_code\">print(\"Anything you want to write\")</span> and you\'ve got your first program working<br>\n</p>\n\n\n','<p>In this statement, we call the print statement to which we supply the text \"hello\nworld\".</p><br>\n\n','#Go ahead, make the computer talk!',100),(3,'Basics','Just printing hello world is not enough, is it? You want to do more than that - you want to take some input, manipulate it and get something out of it. We can achieve this in Python using constants and variables, and we\'ll learn some other concepts as well in this chapter.','For now, just hit run and we will continue our lesson','print(\"Aleluia\")',100),(4,'Comments','Comments are any text to the right of the # symbol and is mainly useful as notes for the reader of the program.\n\nFor example:\n\nprint(\'hello world\') # Note that print is a function\n\nor:\n\n# Note that print is a function\nprint(\'hello world\')\nUse as many useful comments as you can in your program to:\n\n    explain assumptions\n    explain important decisions\n    explain important details\n    explain problems you\'re trying to solve\n    explain problems you\'re trying to overcome in your program, etc.\n','Code tells you how, comments should tell you why.\n\nThis is useful for readers of your program so that they can easily understand what the program is doing. Remember, that person can be yourself after six months!','#This is an example of a comment\n#Comment the line\'s below, or else, the code will produce an error\n\nThis means nothing to the computer, so you better comment it!\nRemember, computer\'s understand they\'re specific language, not human language.\nWell, maybe not yet!',250),(5,'Literal Constants','An example of a literal constant is a number like 5, 1.23, or a string like \'This is a string\' or \"It\'s a string!\".\n\nIt is called a literal because it is literal - you use its value literally. The number 2 always represents itself and nothing else - it is a constant because its value cannot be changed. Hence, all these are referred to as literal constants.','Go ahead and print any literal constans you consider!','#Remember the print, we\'ve learned a few lessons ago!',250),(6,'Numbers','Numbers are mainly of two types - integers and floats.\n\nAn example of an integer is 2 which is just a whole number.\n\nExamples of floating point numbers (or floats for short) are 3.23 and 52.3E-4. The E notation indicates powers of 10. In this case, 52.3E-4 means 52.3 * 10^-4^.','Let\'s print some numbers!','#print your age!\n\n\n\n#print how many eyes do you have\n\n\n\n#print your favourite number!',250),(7,'Strings','A string is a sequence of characters. Strings are basically just a bunch of words.\n\nYou will be using strings in almost every Python program that you write, so pay attention to the following part.\n\nSingle Quote\n\nYou can specify strings using single quotes such as \'Quote me on this\'.\n\nAll white space i.e. spaces and tabs, within the quotes, are preserved as-is.\nDouble Quotes\n\nStrings in double quotes work exactly the same way as strings in single quotes. An example is \"What\'s your name?\".','Print a string single quoted, then a string double quoted!','',250),(8,'Strings are immutable','This means that once you have created a string, you cannot change it. Although this might seem like a bad thing, it really isn\'t. We will see why this is not a limitation in the various programs that we see later on.','Print your name just to get to know you better!','',250),(9,'Variable','Using just literal constants can soon become boring - we need some way of storing any information and manipulate them as well. This is where variables come into the picture. Variables are exactly what the name implies - their value can vary, i.e., you can store anything using a variable. Variables are just parts of your computer\'s memory where you store some information. Unlike literal constants, you need some method of accessing these variables and hence you give them names.','Analyze the code, tested, modify it if you want and submit it!','# a variable can hold a number\n\na = 23\n\n#a variable can hold a string\n\nb = \"Hellooo\"\n\n#and they both can be printed!\n\nprint(a)\nprint(b)',200),(10,'Identifier Naming','Variables are examples of identifiers. Identifiers are names given to identify something. There are some rules you have to follow for naming identifiers:\n\n    The first character of the identifier must be a letter of the alphabet (uppercase ASCII or lowercase ASCII or Unicode character) or an underscore (_).\n    The rest of the identifier name can consist of letters (uppercase ASCII or lowercase ASCII or Unicode character), underscores (_) or digits (0-9).\n    Identifier names are case-sensitive. For example, myname and myName are not the same. Note the lowercase n in the former and the uppercase N in the latter.\n    Examples of valid identifier names are i, name_2_3. Examples of invalid identifier names are 2things, this is spaced out, my-name and >a1b2_c3.\n','Give a variable a value and print it to the console!','',300),(11,'Simple Math','This will be edited','sum two numbers and give it to the docker',' ',700),(12,'Your first operators','Most statements (logical lines) that you write will contain expressions. A simple example of an expression is 2 + 3. An expression can be broken down into operators and operands.  Operators are functionality that do something and can be represented by symbols such as + or by special keywords. Operators require some data to operate on and such data is called operands. In this case, 2 and 3 are the operands','Add two numbers and print them.',' ',700),(13,'Addition','The \"+\" symbol is reserved for adding stuff in python. Adding two numbers it\'s simple as 1+2+3. Just write this and print it. Just like in the same lesson, I know it\'s the same thing, but repeating is always a good practice!','Just add any kind of numbers and print them!',' ',700),(14,'Multiplying','You know that 2+2+2+2 it\'s basically 4 times adding a two? Haha, you know the drill!','Multiply some example, we are onto the big stuff!',' ',700),(15,'Divide and Subtract','Division is the evil brother of multiplying and subtract is the evil sister of addition. ','If i give you 6 - 3 / 3 , what is the answer? Just print that in the console!','#',700),(16,'The new one: MODULO','This is a frequent operator used in programming, it does so little, but it helps us developers so much. It\'s called module and it\'s symbol is \"%\". What the module does? It gives you the rest of the division of a number to another one. Examples: 5 % 2 = 1 (because 5 = 2 * 2 + 1, there is your 1)','How much is 11%10, 15%2, 15 % 3 and 100 % 99?',' ',900),(17,'Expressions','Another handy stuff in programming are the relational expressions. We need to define, check, constraint something to be somehow about another thing everytime! It\'s about the symbols \"<\", \">\" and \"==\". They tell us how big,small,equal is something in relation with something else.','Let\'s print some obvious relations, such as 2 < 3, 5>10 , 5 == 5, 5 >= 5, 10 < 4, 10 >4','# you will find the results are pretty human readable',1000),(18,'The if statement','The if statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block), else we process another block of statements (called the else-block). The else clause is optional.','See the example below','if 2 == 2: print(\"2 is indeed equal to two\")',600),(19,'How the If works',' Often a computer program must make choices on which way to proceed, e.g., if the ball is in bounds, do one thing, else, do something different... if the data has all been processed, end the program, else continue to the next data item... while the player has lives left continue the game.  These \"things\" are called Conditions. Usually this is in the form of a mathematical statment using equals, less-than, or greater-than. ','Compare if a sum of two numbers equals another one and print it!',NULL,800),(20,'What ELSE can I say?','The ELSE keyword (else) let\'s you to run a piece of code if one of your if\'s it\'s not working.','Write something like: If this does not work, else do this!',NULL,1000),(21,'The while loop','The while statement allows you to repeatedly execute a block of statements as long as a condition is true. A while statement is an example of what is called a looping statement. A while statement can have an optional else clause.',NULL,'index = 0 while index < 10: print(\"Currently at step \" + index) index++',700),(22,'The FOR loop','The for..in statement is another looping statement which iterates over a sequence of objects i.e. go through each item in a sequence. We will see more about sequences in detail in later chapters. What you need to know right now is that a sequence is just an ordered collection of items.',NULL,'for i in range(1, 5):     print(i) else:     print(\'The for loop is over\')',700),(23,'The break Statement ','The break statement is used to break out of a loop statement i.e. stop the execution of a looping statement, even if the loop condition has not become False or the sequence of items has not been completely iterated over.  An important note is that if you break out of a for or while loop, any corresponding loop else block is not executed.',NULL,'i = 10 print(\'Final countdown: \') while True: 	if i == 0: 		print(\'Happy Birthday 2018!\')  	else: 		print(i)',800),(24,'The continue Statement ','The continue statement is used to tell Python to skip the rest of the statements in the current loop block and to continue to the next iteration of the loop.',NULL,'i = 10 while True: 	if i%2 == 0:		 		continue  	else: 		print(i)',900),(25,'Breaking down the loops','Write a program that runs 101 loops and at every 5 loops it prints \'Hello World\'',NULL,NULL,1200);
/*!40000 ALTER TABLE `lesson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (2,'admin',NULL),(9,'user',NULL),(10,'user',NULL),(11,'user',NULL),(12,'user',NULL),(13,'user',NULL),(14,'user',NULL),(15,'user',NULL),(16,'user',NULL),(17,'user',NULL),(18,'user',NULL),(19,'user',NULL),(20,'user',NULL);
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(512) DEFAULT NULL,
  `elo_rating` float DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (7,NULL,'ion123@gmail.com','$2b$12$LcvRC3ToC84VxjH7MDaGuuZy/vjz91zPoZdK9v8/FvN6ueZKfDIe2',1200.06,NULL,9),(8,NULL,'abc123@gmail.com','$2b$12$oTKMZh.3UDqYfxQx/WHKaOM3s5lkYb8b.dqHvKEThZws0xyPDMJ/6',1200.04,NULL,10),(11,NULL,'new123@gmail.com','$2b$12$UNU9MreF4ZwkgQ07awRoR.IeSfI1LZ6foYqg4uQpiUMXNEcG23NPq',1200,NULL,13),(12,NULL,'val123@gmail.com','$2b$12$8i6QMp7WJHg8.C/W9HWuo.YLgm3lp7enGt1ccu6fA617dRl0rWAVK',1200,NULL,14),(13,NULL,'unu@gmail.com','$2b$12$313kLkcZgIHZTUQOTxpRA.5hZ7bGooVm9uMfw/UJCDjgNpfoMnVA6',1200,NULL,15),(14,NULL,'edy123@gmail.com','$2b$12$oMz7MAaL.fDlPJ5P0ofSW.oCcYaO.XoBbJ/EPrbOm9A/zFWBUH0ZS',1188.58,NULL,16),(15,NULL,'silviu123@gmail.com','$2b$12$6lE6OF6m3hSlqUzRy9suCe0zpAZBF1E2S./Heg3JGM0IQhYztD6fq',1200.02,NULL,17),(16,NULL,'test123@gmail.com','$2b$12$H0Xuei.3hoW19paLk1DqV.cF1EI1QzotH5FzBxB//KSISjM1sTj.e',1201.1,NULL,18),(18,NULL,'qwe123@gmail.com','$2b$12$BWr0VqR17XzKFkJDxBclNu579IUUl74nt4XVOSuGrDkpoaIjSZgrG',1159.08,NULL,20);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_exercise_difficulty`
--

DROP TABLE IF EXISTS `user_exercise_difficulty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_exercise_difficulty` (
  `user_id` int(11) NOT NULL,
  `exercise_id` int(11) NOT NULL,
  `elo_rating` float DEFAULT NULL,
  `completed` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`exercise_id`),
  KEY `usr_ex_fk2_idx` (`exercise_id`),
  CONSTRAINT `usr_ex_fk1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `usr_ex_fk2` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_exercise_difficulty`
--

LOCK TABLES `user_exercise_difficulty` WRITE;
/*!40000 ALTER TABLE `user_exercise_difficulty` DISABLE KEYS */;
INSERT INTO `user_exercise_difficulty` VALUES (7,1,5,0),(8,1,2,0),(14,1,611.751,1),(14,2,599.673,1),(14,3,600,0),(18,1,599.694,1),(18,2,599.693,1),(18,3,602.11,1),(18,4,599.691,1),(18,6,1501.24,0),(18,12,800,0);
/*!40000 ALTER TABLE `user_exercise_difficulty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_lesson_difficulty`
--

DROP TABLE IF EXISTS `user_lesson_difficulty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_lesson_difficulty` (
  `user_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `elo_rating` float NOT NULL,
  `COMPLETED` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`user_id`,`lesson_id`),
  KEY `lesson_id` (`lesson_id`),
  CONSTRAINT `user_lesson_difficulty_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `user_lesson_difficulty_ibfk_2` FOREIGN KEY (`lesson_id`) REFERENCES `lesson` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_lesson_difficulty`
--

LOCK TABLES `user_lesson_difficulty` WRITE;
/*!40000 ALTER TABLE `user_lesson_difficulty` DISABLE KEYS */;
INSERT INTO `user_lesson_difficulty` VALUES (7,1,99.9822,1),(7,2,99.9823,1),(7,3,99.9823,1),(7,4,250,0),(7,5,250,0),(7,6,250,0),(7,7,249.958,1),(7,8,250,0),(7,9,200,0),(7,10,300,0),(11,1,100,0),(11,2,100,0),(11,3,100,0),(11,4,250,0),(11,5,250,0),(11,6,250,0),(11,7,250,0),(11,8,250,0),(11,9,200,0),(11,10,300,0),(11,11,700,0),(11,12,700,0),(11,13,700,0),(11,14,700,0),(11,15,700,0),(11,16,900,0),(11,17,1000,0),(12,1,100,0),(12,2,100,0),(12,3,100,0),(12,4,250,0),(12,5,250,0),(12,6,250,0),(12,7,250,0),(12,8,250,0),(12,9,200,0),(12,10,300,0),(12,11,700,0),(12,12,700,0),(12,13,700,0),(12,14,700,0),(12,15,700,0),(12,16,900,0),(12,17,1000,0),(13,1,100,0),(13,2,100,0),(13,3,100,0),(13,4,250,0),(13,5,250,0),(13,6,250,0),(13,7,250,0),(13,8,250,0),(13,9,200,0),(13,10,300,0),(13,11,700,0),(13,12,700,0),(13,13,700,0),(13,14,700,0),(13,15,700,0),(13,16,900,0),(13,17,1000,0),(14,1,99.9822,1),(14,2,109.982,0),(14,3,100,0),(14,4,250,0),(14,5,250,0),(14,6,250,0),(14,7,250,0),(14,8,250,0),(14,9,200,0),(14,10,300,0),(14,11,700,0),(14,12,700,0),(14,13,700,0),(14,14,700,0),(14,15,700,0),(14,16,900,0),(14,17,1000,0),(15,1,99.9822,1),(15,2,100,0),(15,3,100,0),(15,4,250,0),(15,5,250,0),(15,6,250,0),(15,7,250,0),(15,8,250,0),(15,9,200,0),(15,10,300,0),(15,11,700,0),(15,12,700,0),(15,13,700,0),(15,14,700,0),(15,15,700,0),(15,16,900,0),(15,17,1000,0),(16,1,99.9822,1),(16,2,99.9823,1),(16,3,100,0),(16,4,250,0),(16,5,250,0),(16,6,250,0),(16,7,250,0),(16,8,250,0),(16,9,200,0),(16,10,300,0),(16,11,700,0),(16,12,700,0),(16,13,699.468,1),(16,14,699.469,1),(16,15,700,0),(16,16,900,0),(16,17,1000,0),(18,1,99.9775,1),(18,2,99.9775,1),(18,3,100,0),(18,4,250,0),(18,5,250,0),(18,6,250,0),(18,7,250,0),(18,8,250,0),(18,9,200,0),(18,10,300,0),(18,11,700,0),(18,12,700,0),(18,13,700,0),(18,14,700,0),(18,15,700,0),(18,16,900,0),(18,17,1000,0),(18,18,638.539,0),(18,19,800,0),(18,20,1000,0),(18,21,700,0),(18,22,700,0),(18,23,800,0),(18,24,900,0),(18,25,1200,0);
/*!40000 ALTER TABLE `user_lesson_difficulty` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-01 20:33:12
