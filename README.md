# EventSeg-demo

#### In this repo, we are testing functionality and executability of `brainiak.eventseg.event.EventSegment` to prepare for later analyses of our own data.

# Using this repo

#### The brainiak environment and setup as well as other dependencies are included in `environment.yml`. To begin start by cloning this repository.

```bash
git clone https://github.com/w-decker/EventSeg-demo.git

```

#### Next activate the brainiak environment (brainiak_env).

```bash
conda create -f brainiak_env.yml
```

#### If you receive errors regarding ipykernel (hopefully you will not), try the following in the terminal.

```bash
$ conda install -n brainiak_env ipykernel --update-deps --force-reinstall
```
