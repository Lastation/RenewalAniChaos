import Function as f;

function Shape(cp : TrgPlayer, count, Unit : TrgUnit);
function ShapeWithProperty(cp : TrgPlayer, count, Unit : TrgUnit, property);


function main(cp)
{
   f.BanReturn(cp);
   f.HoldPosition(cp);

   MoveUnit(All, "60 + 1n High Templar", cp, "Anywhere", "[Skill]HoldPosition");

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            Shape(cp, 1, "60 + 1n High Templar");
            Shape(cp, 1, "60 + 1n Archon");
            ShapeWithProperty(cp, 1, "40 + 1n Gantrithor", 1);

            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);
         }

         if (f.loop[cp] == 2)
         {
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            Shape(cp, 1, "40 + 1n Mojo");

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         }

         if (f.loop[cp] == 4)
         {
            RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            Shape(cp, 1, "60 + 1n Danimoth");
            ShapeWithProperty(cp, 1, "40 + 1n Lurker", 0);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Lurker", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }

         if (f.loop[cp] == 8)
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 14)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         f.MoveLoc("40 + 1n Lurker", cp, 0, 0);
         RemoveUnitAt(1, "40 + 1n Lurker", "Anywhere", cp);
         f.SkillUnit(cp, 1, "60 + 1n Archon");
         f.SkillUnitWithProperty(cp, 1, "60 + 1n Danimoth", 1);

         KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 16)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         f.SkillEnd(cp);
      }
   }
}

function Shape(cp : TrgPlayer, count, Unit : TrgUnit)
{
   f.SquareShape(cp, count, Unit, 50, 0);
   f.SquareShape(cp, count, Unit, 100, 100);
   f.SquareShape(cp, count, Unit, 150, 0);
   f.SquareShape(cp, count, Unit, 50, 50);
}

function ShapeWithProperty(cp : TrgPlayer, count, Unit : TrgUnit, property)
{
   f.SquareShapeWithProperty(cp, count, Unit, 50, 0, property);
   f.SquareShapeWithProperty(cp, count, Unit, 100, 100, property);
   f.SquareShapeWithProperty(cp, count, Unit, 150, 0, property);
   f.SquareShapeWithProperty(cp, count, Unit, 50, 50, property);
}
