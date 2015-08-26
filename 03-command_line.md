# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.


    pwd — print working directory
    mkdir — create new directory
    mkdir -p — create nested directory
    cd — home directory 
    cd [directory] — change directory
    ls — lists the names of the files and/or directories in the current directory
    rm -r [directory] — remove a directory and contents 
    cp *.jpg ~/Documents — copy all the files with names ending in .jpg into Documents directory
    mv name newname — change the name of the file from name to newname
    cat > [file] — create a blank txt file or overwrites the existing file
    cat >> [file] — adds text to existing file 
        (contol plus d keys to execute and cancel cat)
    grep “string” [file] — search “string” in [file]

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?


    ls — lists the names of the files and/or directories in the current directory, short listing
    ls -a — lists the names of the files and/or directories, including hidden files, in the current directory
    ls -l — lists detailed directory contents, long listing
    ls -lh — long listing with sizes (byte, kilobyte etc)
    
    ls -lh and ls -a makes more sense than ls -l


---


---

What does `xargs` do? Give an example of how to use it.


    As i understand, xargs is useful when it is combined with other commands. 
    "Tasks that may have previously seemed unmanageable, such as processing hundreds of files individually, can be       performed easily with xargs." 

    Following example i found shows that it is possible to complete an operation in a single step instead of doing it     for each file.

    I created a directory called xargstest on desktop. xargstest has 3 directory called dir1, dir2 and dir3 and each     of these directories has .txt files inside.

          find xargstest/ -name “file**” | sort | xargs wc -l

    The find command identifies and lists the files in xargstest and all of its subdirectories. The -name ‘file**’       option specifies only files with names beginning with "file" followed by any two characters in the xargstest         directory.
    
    Piping the results with sort command orders the filenames sequentially.

    wc command with the -l option counts the number of newlines in each file. Here is the result:

         1 xargstest/dir1/file1A
         2 xargstest/dir1/file1B
         8 xargstest/dir2/file2A
         4 xargstest/dir2/file2B
         1 xargstest/dir3/file3A
         6 xargstest/dir3/file3B
        22 total


---

