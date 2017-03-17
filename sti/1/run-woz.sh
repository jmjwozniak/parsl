#!/bin/sh
set -eu

# RUN-WOZ
# This is just a convenience script for Wozniak

PATH=$HOME/sfw/swift-t/stc/bin:$HOME/sfw/Python-2.7.10/bin:$PATH
export PYTHONPATH=$HOME/sfw/Python-2.7.10/lib/python2.7:$PWD

swift-t -l -n 5 workflow.swift
