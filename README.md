# schwinger-vqe
VQE simulation of the Schwinger model with Qiskit

VQE Calculations

- savage.ipynb is the original Jupyter notebook used to play with VQE workflow. It uses Qiskit minimally, so that all the different parts are
explicit and verbose. This may be helpful when trying to understand what
Qiskit does behind the scenes.
- VQE.ipynb is the main notebook for a VQE simulations. Still in development. 
Ultimately, this needs be a Python module/package.
But the current Jupyter-notebook form is convenient for playing around with the code and learning Qiskit's functionality. 
Different parts of the VQE workflow have smaller notebooks. They're not required to run the main one, 
but are convenient if you want to look at an isolated element of the simulation.
- Superposition.ipynb is the Jupyter with a circuit for producing a superposition of the variational states (ground state and first excited state)

Mathematica code (exact diagonalization)

- savage.nb is the main notebook that performs projection onto
zero-momentum sector, truncation, and splits the resulting Hilbert space
into even and odd parity sectors. It diagonalizes the corresponding Hamiltonians,
expresses the eigenstates in the computational basis of the QC
simulation. Interpolating operators are constructed and exact effective
mass curves are computed. 
- variational_layer.nb is a notebook to play
with the form of the variational layer in the QC simulation as an
explicit unitary. 
- operators.nb is a notebook where the numerical matrix
form of the interpolators is computed in the (concatenated) QC
computational basis of even and odd parity sectors.

## Tentative plan for the Hackathon (Arthur):

- Catch up on background of VQE: this [reference](https://arxiv.org/pdf/1704.05018.pdf) may be useful.
- Walk through the existing code together (*VQE.ipynb*) to make sure everyone is up to speed. I'll answer questions about the physical model and the exact solution too, to the best of my ability :)
- Debrief and discuss options of what we can do next, and how we could split our efforts. The key steps are:  
  1. Run the code we have on the quantum computer backend and compare against our exact solutions, to see how bad the noise is. A lot of activity on analyzing and mitigating errors could spur from here, and I would love to work on this, perhaps with Chris?
  2. Try to scale up the simulation to larger volume: answer the question, how does the variational form (the circuit) change when we have 4 or 6 qubits instead of 2? I can provide some more information on this.
  3. Work on measurements for a *transition matrix* element. I'll give information on that as well.
