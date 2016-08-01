sudo apt-get update -y
sudo apt-get install -y git
wget -c http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
bash Miniconda-latest-Linux-x86_64.sh -b -p ~/miniconda
export PATH=~/miniconda/bin:$PATH
conda install -y numpy scipy pandas jupyter matplotlib

conda install pip
pip install cython
sudo apt-get install -y g++ htop
pip install git+git://github.com/scikit-learn/scikit-learn.git

jupyter notebook --no-browser --ip 0.0.0.0 &
disown
