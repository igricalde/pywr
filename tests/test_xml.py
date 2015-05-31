#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import pandas
import datetime

import pywr.core
import pywr.xmlutils

from helpers import load_model

def test_simple1():
    '''Test parsing a simple XML document'''
    # parse the XML into a model
    model = load_model('simple1.xml')

    # metadata
    assert(model.metadata['title'] == 'Simple 1')
    assert(model.metadata['description'] == 'A very simple example.')

    # node names
    nodes = model.nodes()
    assert(len(nodes) == 3)
    name_to_node = {}
    for node in nodes:
        name_to_node[node.name] = node
    supply1 = name_to_node['supply1']
    link1 = name_to_node['link1']
    demand1 = name_to_node['demand1']

    # node types
    assert(type(supply1) is pywr.core.Supply)
    assert(type(link1) is pywr.core.Link)
    assert(type(demand1) is pywr.core.Demand)

    # node positions
    assert(supply1.position == (1,1))
    assert(link1.position == (2,1))
    assert(demand1.position == (3,1))

    model.check()

def test_timestamps():
    '''Test datetime related model parameters'''
    model = load_model('timeseries1.xml')
    
    assert(model.parameters['timestamp_start'] == pandas.to_datetime('1970-01-01'))
    assert(model.parameters['timestamp_finish'] == pandas.to_datetime('3027-08-22'))
    assert(model.parameters['timestep'] == datetime.timedelta(1))
    