require 'spec_helper'

describe Post do

  it "should create a post" do
    expect { FactoryGirl.create(:post) }.to change(Post, :count).by(1)
  end

  it "should not create a post without a title" do
    FactoryGirl.build(:post, title: nil).should_not be_valid
  end

  it "should not create a post without a body" do
    FactoryGirl.build(:post, body: nil).should_not be_valid
  end

  it "should have a unique title" do
    FactoryGirl.create(:post, title: "not unique title")
    FactoryGirl.build(:post, title: "not unique title").should_not be_valid
  end

end