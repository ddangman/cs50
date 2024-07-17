# Combine geom_line and geom_point

load("anita.RData")

# points behind line looks bad
ggplot(anita, aes(x = timestamp, y = wind)) +
  geom_point(color = "deepskyblue4", size=5) +
  geom_line(size=3)


# points in front of line looks good
ggplot(anita, aes(x = timestamp, y = wind)) +
  geom_line(size=3) +
  geom_point(color = "deepskyblue4", size=5)
