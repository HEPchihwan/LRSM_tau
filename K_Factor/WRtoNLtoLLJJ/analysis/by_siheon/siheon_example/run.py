import sys
import pyhepmc as hep
import numpy as np

class HepMCFilter:
    def __init__(self):
        pass
    def SetInput(self, input_file):
        self.input = hep.open(input_file)
    def SetOutput(self, output_file):
        self.output = hep.open(output_file, "w")
    def SetFilterParameters(self, pdgid, r_threshold, z_threshold):
        self.pdgid = pdgid
        self.r_threshold = r_threshold
        self.z_threshold = z_threshold
    def Run(self):
        for ev in self.input:
            ptls = ev.particles
            record = False
            for ptl in ptls:
                if ptl.pid == self.pdgid:
                    rho = ptl.end_vertex.position.rho()
                    theta = ptl.end_vertex.position.theta()
                    z = rho * np.cos(theta)
                    r = rho * np.sin(theta)
                    if (r < self.r_threshold) and (z < self.z_threshold):
                        record = True
            if record:
                self.output.write(ev)
        self.Close()
    def Close(self):
        self.output.close()
        self.input.close()


filter = HepMCFilter()
filter.SetInput("tag_1_pythia8_events.hepmc")
filter.SetOutput("filtered.hepmc")
filter.SetFilterParameters(32, 100, 100)
filter.Run()
