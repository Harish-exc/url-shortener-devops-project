provider "aws" {
  region = var.aws_region
}

module "vpc" {
  source  = "./vpc.tf"
}

module "eks" {
  source               = "terraform-aws-modules/eks/aws"
  cluster_name         = var.cluster_name
  cluster_version      = "1.27"
  subnets              = module.vpc.private_subnets
  vpc_id               = module.vpc.vpc_id
  cluster_iam_role_name = aws_iam_role.eks_cluster_role.name

  node_groups = {
    default = {
      desired_capacity = 2
      max_capacity     = 3
      min_capacity     = 1
      instance_type    = "t3.medium"
    }
  }
}
