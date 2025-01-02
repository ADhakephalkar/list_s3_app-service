variable "app_name" {
  description = "The name of the application"
  type        = string
  default     = "list_s3_app-service"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami_id" {
  description = "AMI ID for EC2 instance"
  type        = string
  default     = "ami-xxxxxxxxxxxxxxxxx" # Update as needed
}
