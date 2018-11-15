#!/usr/bin/env python

from vafmcircuits import Machine
import math


def main():

    machine = Machine(name='machine', dt=0.01, pushed=True)
    scanner = machine.AddCircuit(type='Scanner', name='scan', pushed=True)
    inter = machine.AddCircuit(
        type='i1Dlin', name='inter', comp=2, step=0.1, pbc=True, pushed=True)

    dump = machine.AddCircuit(
        type='output', name='output', file='test_i1Dlin.dat', dump=1)
    dump.Register('global.time', "scan.x", "inter.F1", "inter.F2")

    machine.Connect("scan.x", "inter.x")

    # create a forcefield
    forces = [[math.sin(2*math.pi*x/20), math.cos(2*2*math.pi*x/20)]
              for x in range(20)]
    inter.SetData(forces)

    #machine.SetInput(channel="output.record", value=0)
    # scanner.Place(0,0,500)
    # scanner.Move(0,0,-5)
    # machine.Wait(0.02)
    scanner.Move(x=2, v=1)


if __name__ == '__main__':
    main()
