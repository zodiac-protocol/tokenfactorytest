#[allow(clippy::redundant_field_names)]


pub mod math;
pub mod utils;
pub mod tokenfactory_hooks;

//stargate
#[allow(clippy::derive_partial_eq_without_eq)] //all auto-generated 
pub mod cosmos {
  pub mod base {
    pub mod query{
      pub mod v1beta1{
        include!("protos/cosmos.base.query.v1beta1.rs");
      }
    }
    
    pub mod v1beta1{
      include!("protos/cosmos.base.v1beta1.rs");
    }
  }

  pub mod bank {
    pub mod v1beta1{
      include!("protos/cosmos.bank.v1beta1.rs");
    }
  }
}

#[allow(clippy::derive_partial_eq_without_eq)] //all auto-generated 
pub mod osmosis {

  pub mod gamm {
    pub mod v1beta1{
      include!("protos/osmosis.gamm.v1beta1.rs");
    }

    pub mod poolmodels{
      pub mod balancer {
        pub mod v1beta1 {
          include!("protos/osmosis.gamm.poolmodels.balancer.v1beta1.rs");
        }
      }
    }

  }

  pub mod lockup {
    include!("protos/osmosis.lockup.rs");
  }

  pub mod incentives {
    include!("protos/osmosis.incentives.rs");
  }

  pub mod tokenfactory{
    pub mod v1beta1{
      include!("protos/osmosis.tokenfactory.v1beta1.rs");
    }
  }

}


