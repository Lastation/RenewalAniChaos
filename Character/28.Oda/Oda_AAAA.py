import Function as f;

function main(cp)
{
   f.HoldPosition(cp);
   f.BanReturn(cp);

   MoveUnit(All, "40 + 1n Goliath", cp, "Anywhere", "[Skill]HoldPosition");
   MoveUnit(All, "50 + 1n Tank", cp, "Anywhere", "[Skill]HoldPosition");

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] > 0)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 3, 75);
         }
         if (f.loop[cp] > 1)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 5, 150);
         }
         if (f.loop[cp] > 2)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 7, 225);
         }
         if (f.loop[cp] > 3)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 9, 300);
         }
         if (f.loop[cp] > 4)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 11, 375);
         }
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 32)
         {
            f.Voice_Routine(cp, 2);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 1)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 3, 75);
         }
         if (f.loop[cp] < 2)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 5, 150);
         }
         if (f.loop[cp] < 3)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 7, 225);
         }
         if (f.loop[cp] < 4)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 9, 300);
         }
         if (f.loop[cp] < 5)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 11, 375);
         }

         if (f.loop[cp] == 1)
         {
            f.EdgeShapeBurrowed(cp, 1, "40 + 1n Lurker", 45, 3, 75);
         }
         else if (f.loop[cp] == 2)
         {
            f.EdgeShapeBurrowed(cp, 1, "40 + 1n Lurker", 45, 5, 150);
         }
         else if (f.loop[cp] == 3)
         {
            f.EdgeShapeBurrowed(cp, 1, "40 + 1n Lurker", 45, 7, 225);
         }
         else if (f.loop[cp] == 4)
         {
            f.EdgeShapeBurrowed(cp, 1, "40 + 1n Lurker", 45, 9, 300);
         }
         else if (f.loop[cp] == 5)
         {
            f.EdgeShapeBurrowed(cp, 1, "40 + 1n Lurker", 45, 11, 375);
         }

         if (f.loop[cp] > 5)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 3, 75);
         }
         if (f.loop[cp] > 6)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 5, 150);
         }
         if (f.loop[cp] > 7)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 7, 225);
         }
         if (f.loop[cp] > 8)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 9, 300);
         }
         if (f.loop[cp] > 9)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 11, 375);
         }
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

         RemoveUnitAt(All, "40 + 1n Lurker", "[Skill]Unit_Wait_ALL", cp);

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 14)
         {
            KillUnitAt(All, "40 + 1n Lurker", "Anywhere", cp);
            f.Voice_Routine(cp, 3);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         var i = f.loop[cp];

         for (; i < 10; i++)
         {
            f.LineShape(cp, 1, "60 + 1n High Templar", 90, 11, 75, -75 * 4 + 75 * i);
         }
         if (f.loop[cp] < 11)
         {


         }

         if (f.loop[cp] < 1)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 3, 75);
         }
         if (f.loop[cp] < 2)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 5, 150);
         }
         if (f.loop[cp] < 3)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 7, 225);
         }
         if (f.loop[cp] < 4)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 9, 300);
         }
         if (f.loop[cp] < 5)
         {
            f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 11, 375);
         }



         if (f.loop[cp] == 1)
         {
            f.EdgeShape(cp, 1, "40 + 1n Goliath", 45, 3, 75);
         }
         else if (f.loop[cp] == 2)
         {
            f.EdgeShape(cp, 1, "40 + 1n Goliath", 45, 5, 150);
         }
         else if (f.loop[cp] == 3)
         {
            f.EdgeShape(cp, 1, "40 + 1n Goliath", 45, 7, 225);
         }
         else if (f.loop[cp] == 4)
         {
            f.EdgeShape(cp, 1, "40 + 1n Goliath", 45, 9, 300);
         }
         else if (f.loop[cp] == 5)
         {
            f.EdgeShape(cp, 1, "40 + 1n Goliath", 45, 11, 375);
         }

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

         RemoveUnitAt(All, "40 + 1n Goliath", "[Skill]Unit_Wait_ALL", cp);

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 14)
         {
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            f.Voice_Routine(cp, 4);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] == 1)
         {
            f.EdgeShape(cp, 1, "50 + 1n Tank", 45, 3, 75);
         }
         else if (f.loop[cp] == 2)
         {
            f.EdgeShape(cp, 1, "50 + 1n Tank", 45, 5, 150);
         }
         else if (f.loop[cp] == 3)
         {
            f.EdgeShape(cp, 1, "50 + 1n Tank", 45, 7, 225);
         }
         else if (f.loop[cp] == 4)
         {
            f.EdgeShape(cp, 1, "50 + 1n Tank", 45, 9, 300);
         }
         else if (f.loop[cp] == 5)
         {
            f.EdgeShape(cp, 1, "50 + 1n Tank", 45, 11, 375);
         }

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);

         RemoveUnitAt(All, "50 + 1n Tank", "[Skill]Unit_Wait_ALL", cp);

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 23)
         {
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            f.Voice_Routine(cp, 5);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         if (f.loop[cp] == 1)
         {
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 45, 3, 75);
         }
         else if (f.loop[cp] == 2)
         {
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 45, 5, 150);
         }
         else if (f.loop[cp] == 3)
         {
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 45, 7, 225);
         }
         else if (f.loop[cp] == 4)
         {
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 45, 9, 300);
         }
         else if (f.loop[cp] == 5)
         {
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 45, 11, 375);
         }

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 23)
         {
            f.Voice_Routine(cp, 6);
         }

         if (f.loop[cp] == 48)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            SetSwitch("UiltimateSwitch", Clear);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 5)
      {
         f.SkillEnd(cp);
      }
   }
}