class Post < ActiveRecord::Base
  attr_accessible :body, :category, :published, :title

  validates :body, presence: true
  validates :title, presence: true, uniqueness: true

  scope :for_category, lambda { |category| where(:category => category) }
end
