echo Run as regular user!
echo Remember that you have to login for this service to start.
cp recollecing.service ~/.config/systemd/user/
systemctl --user enable recollecing
