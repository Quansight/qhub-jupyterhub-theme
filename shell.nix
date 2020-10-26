{ pkgs ? import <nixpkgs> {}, pythonPackages ? pkgs.python3Packages }:

pkgs.mkShell {
  buildInputs = [
    pythonPackages.jupyterhub

    # keep this line if you use bash
    pkgs.bashInteractive
  ];
}
