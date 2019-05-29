dbrecon.py is a collection of functions that were developed to assist in the databse reconstruction code. Much of this allows us to easily move the code around and have it work with either local file systems or Amazon's S3.

Functions you can use in dbrecon:

s3open(path, [mode=mode], encoding=encoding) --- Open a file on Amazon S3 for reading or writing.

dopen(path, [mode=mode], [encoding=encoding]) --- Open a file either on local file system or Amazon S3. 
   Substitutes $ROOT and $SRC

dsystem() - Like system, but raises error if there is an error.  Logs system call

To use Logging, you will call two functions:

   get_config() -- Returns a config file (filename default is config.ini)
   setup_logging(level) --- Called after option parsing, establishing logging level.

Here is how you use it:

    if __name__=="__main__":
        config = dbrecon.get_config()
        from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
        parser = ArgumentParser( formatter_class = ArgumentDefaultsHelpFormatter,
                                 description="Read SF1 geography files" )
        dbrecon.argparse_add_logging(parser)
        parser.add_argument("state_abbr")
        args = parser.parse_args()
        dbrecon.setup_logging(args.loglevel)
   




