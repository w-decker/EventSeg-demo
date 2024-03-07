# EventSeg-demo

#### In this repo, we are testing functionality and executability of `brainiak.eventseg.event.EventSegment` to prepare for later analyses of our own data.

# Using this repo

#### The brainiak environment and setup as well as other dependencies are included in `environment.yml`. To begin start by cloning this repository.

```bash
git clone https://github.com/w-decker/EventSeg-demo.git

```

#### Next activate the brainiak environment (brainiak_env).
If you are working on relearn0.lsu.edu, you should be able to use the shared `brainiack_env` at `/data/.conda/envs/brainiak_env`. In VSCode, `ctrl+shift+p` to get the command prompt, then "Select Python Interpretter", and choose this environment from the list.

If you need to install a non-shared version, you could do:

```bash
conda create --name brainiak_env
conda install --name brainiak_env -c brainiak -c defaults -c conda-forge brainiak scikit-learn-intelex ipykernel nilearn deepdish
```

#### If you receive errors regarding ipykernel (hopefully you will not), try the following in the terminal.

```bash
$ conda install -n brainiak_env ipykernel --update-deps --force-reinstall
```
