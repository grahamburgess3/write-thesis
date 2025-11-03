sample <- scan(file = "stdin", quiet = TRUE)

pdf("histogram.pdf", width = 7, height = 5)

hist(
  sample,
  main = "Sample from triangle distribution",
  xlab = "Values",
  col = "skyblue",
  border = "white"
)

dev.off()