# -*- coding: utf-8 -*-


class CommandLineInterface:

    def __init__(self, parser):
        """
        Initializes a CommandLineInterface instance.

        :param parser: the arguments parser.
        """
        self.parser = parser

   def run(self):
        """
        Run this command-line tool.
        """
        raise NotImplementedError('run() is not implemented!')
