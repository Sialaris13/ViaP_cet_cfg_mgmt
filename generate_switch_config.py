from jinja import load_data, render_device, write_config

data = load_data()

data = data['switch_config']
print(data)


class device:
  def __init__(self, name, **data):
    self.name = name

    self.type = 'test'
    self.ap = data.get("ap")
    self.vvs = data.get("vvs")
    self.vrs = data.get("vrs")
    self.icmv = data.get("icmv")
    self.captel = data.get("captel")

  @property
  def num_aps(self):
    return len(self.ap)

  def __repr__(self):
    return self.name

devices = []

# loop through the dictionary and create the device objects
for switch_name, data in data.items():
  new_device = device(switch_name, **data)
  devices.append(new_device)


# pass each device to the jinja template 
for device in devices:
  output = render_device("switch_config.j2", device)
  write_config(output, device.name)



